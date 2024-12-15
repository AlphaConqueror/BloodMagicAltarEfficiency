# Rune space per tier
RUNE_SPACE_TIER_2 = 8
RUNE_SPACE_TIER_3 = 28
RUNE_SPACE_TIER_4 = 56
RUNE_SPACE_TIER_5 = 108
RUNE_SPACE_TIER_6 = 184

# Client Input
AVERAGE_MOB_COUNT = 20
RUNE_SPACE = RUNE_SPACE_TIER_6

# Blood Magic defaults
DEFAULT_CAPACITY = 10000
DEFAULT_TICK_FACTOR = 20
DEFAULT_TRANSMISSION_RATE = 20
MAX_RUNES_OF_ACCELERATION = 19
RUNE_OF_SACRIFICE_GAIN_PERCENT = 10
WELL_OF_SUFFERING_TICKS = 25

# other
DEBUG = False
USE_SUPERIOR_CAPACITY_AT = 15  # DEFAULT_CAPACITY * 1.1^n >= DEFAULT_CAPACITY + 2000 * n


class Data:
    rune_space_left = RUNE_SPACE
    # number of ticks before the next processing
    current_tick_factor = DEFAULT_TICK_FACTOR
    runes_of_dislocation = 0
    runes_of_acceleration = 0
    # equals runes of superior capacity, if runeOfCapacity >= USE_SUPERIOR_CAPACITY_AT
    runes_of_capacity = 0
    runes_of_sacrifice = 0


class RuneType:
    DISLOCATION = 0
    ACCELERATION = 1
    CAPACITY = 2
    SACRIFICE = 3


def add_rune(data: Data, rune_type: int, amount: int):
    for _ in range(0, amount):
        match rune_type:
            case RuneType.DISLOCATION:
                if calc_transfer_rate(data) > get_buffer(data):
                    data.runes_of_capacity += 1
                else:
                    data.runes_of_dislocation += 1

            case RuneType.ACCELERATION:
                if data.runes_of_acceleration >= MAX_RUNES_OF_ACCELERATION:
                    raise Exception("Amount of runes of acceleration exceed the max of "
                                    + str(MAX_RUNES_OF_ACCELERATION) + ".")

                data.runes_of_acceleration += 1
                data.current_tick_factor -= 1

            case RuneType.CAPACITY:
                data.runes_of_capacity += 1

            case RuneType.SACRIFICE:
                data.runes_of_sacrifice += 1

            case _:
                raise Exception()

        data.rune_space_left -= 1


# transfer rate is limited by the buffer
# in LP/current_tick_factor ticks
def calc_transfer_rate(data: Data) -> float:
    return DEFAULT_TRANSMISSION_RATE / data.current_tick_factor * pow(1.2, data.runes_of_dislocation)


# every mob generates 10 LP per damage instance
# in LP
def calc_generation_rate(data: Data) -> float:
    return AVERAGE_MOB_COUNT * 10 * (1 + data.runes_of_sacrifice * 0.1)


# in LP
def get_capacity(data: Data) -> float:
    return DEFAULT_CAPACITY + 2000 * data.runes_of_capacity \
        if data.runes_of_capacity < USE_SUPERIOR_CAPACITY_AT \
        else DEFAULT_CAPACITY * pow(1.1, data.runes_of_capacity)


# equals to max transfer rate
# in LP/current_tick_factor ticks
def get_buffer(data: Data) -> float:
    return 0.1 * get_capacity(data) / data.current_tick_factor


def print_data(data: Data) -> None:
    print("WELL OF SUFFERING TICKS: ", WELL_OF_SUFFERING_TICKS,
          '\n' + "AVERAGE MOB COUNT: ", AVERAGE_MOB_COUNT,
          '\n' + "RUNE SPACE: ", RUNE_SPACE,
          '\n' + "RUNES OF DISLOCATION: ", data.runes_of_dislocation,
          '\n' + "RUNES OF ACCELERATION: ", data.runes_of_acceleration,
          '\n' + "RUNES OF " + (
              "AUGMENTED" if data.runes_of_capacity < USE_SUPERIOR_CAPACITY_AT else "SUPERIOR") + " CAPACITY: ",
          data.runes_of_capacity,
          '\n' + "RUNES OF SACRIFICE: ", data.runes_of_sacrifice,
          '\n' + "TICK FACTOR: ", data.current_tick_factor,
          '\n' + "TRANSFER RATE: ", calc_transfer_rate(data), "LP/" + str(data.current_tick_factor) + "t (",
          (calc_transfer_rate(data) / data.current_tick_factor),
          "LP/t ); within " + str(WELL_OF_SUFFERING_TICKS) + " ticks: ",
          calc_transfer_rate(data) * (WELL_OF_SUFFERING_TICKS // data.current_tick_factor),
          '\n' + "GENERATION RATE: ", calc_generation_rate(data), "LP/" + str(WELL_OF_SUFFERING_TICKS) + 't'
          + '\n' + "BUFFER: ", get_buffer(data), "LP/" + str(data.current_tick_factor) + "t (",
          get_buffer(data) / data.current_tick_factor, "LP/t );"
          + '\n' + "CAPACITY: ", get_capacity(data), "LP")


def print_small_data(data: Data) -> None:
    print("TRANSFER RATE: ", calc_transfer_rate(data), "LP/" + str(data.current_tick_factor) + "t (",
          (calc_transfer_rate(data) / data.current_tick_factor), "LP/t )"
          + '\n' + "GENERATION RATE: ", calc_generation_rate(data), "LP/" + str(WELL_OF_SUFFERING_TICKS) + 't')


if __name__ == '__main__':
    best_data = None

    # take samples of setup using 0 to MAX_RUNES_OF_ACCELERATION runes of acceleration
    # and take the one with the highest generation rate
    for i in range(0, MAX_RUNES_OF_ACCELERATION + 1):
        data: Data = Data()

        add_rune(data, RuneType.ACCELERATION, i)

        if DEBUG:
            print("--------------------")
            print_small_data(data)

        while data.rune_space_left > 0:
            # ensure big enough capacity to take in all the generated LP
            if calc_generation_rate(data) > get_capacity(data):
                add_rune(data, RuneType.CAPACITY, 1)
            elif calc_generation_rate(data) < (
                    min(get_buffer(data), calc_transfer_rate(data)) * WELL_OF_SUFFERING_TICKS):
                add_rune(data, RuneType.SACRIFICE, 1)
            else:
                add_rune(data, RuneType.DISLOCATION, 1)

            if DEBUG:
                print_small_data(data)

        if DEBUG:
            print_data(data)

        if best_data is None or calc_generation_rate(data) > calc_generation_rate(best_data):
            best_data = data

    print_data(best_data)
