"""Calculate how long it takes to prepare and bake a lasagna."""

EXPECTED_BAKE_TIME = 40 # Time in minutes.
PREPARATION_TIME = 2 # Time in minutes.


def bake_time_remaining(elapsed_bake_time):
    """Return the bake time remaining.

    The elapsed_bake_time is the time the lasagna has been in the oven
    and the return value is the time left to finish baking in minutes.

    >>> bake_time_remaining(15)
    25

    >>> bake_time_remaining(40)
    0
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Return the preparation time in minutes.

    The number_of_layers is multiplied by the time it takes to prepare
    a layer.

    >>> preparation_time_in_minutes(2)
    4
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return the elapsed cooking time.

    The elapsed_bake_time is added to the preparation time of
    number_of_layer.

    >>> elapsed_time_in_minutes(3, 20)
    26
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
