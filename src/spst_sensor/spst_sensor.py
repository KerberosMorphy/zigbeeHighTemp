from __future__ import annotations

from time import sleep
from typing import Optional

CREOSOTE_THRESHOLD = 0
OVERFIRE_THRESHOLD = 0
OVERFIRE_ALARM_THRESHOLD = 1.2 * OVERFIRE_THRESHOLD

CREOSOTE_LED_2_THRESHOLD_RATIO = 0.5
OPTIMAL_LED_2_THRESHOLD_RATIO = 0.9
OPTIMAL_LED_3_THRESHOLD_RATIO = 0.9

BASE_LED_STATE = (True, False, False, False, False, False, False)


class SPSTSensor:
    def __init__(self) -> None:
        self.creosote_threshold = CREOSOTE_THRESHOLD
        self.overfire_threshold = OVERFIRE_THRESHOLD
        self.alarm_threshold = OVERFIRE_ALARM_THRESHOLD
        self.led_states = BASE_LED_STATE

    def set_threshold(
        self, creosote_threshold: Optional[int] = None, overfire_threshold: Optional[int] = None
    ) -> None:
        if creosote_threshold is not None:
            self.creosote_threshold = creosote_threshold
        if overfire_threshold is not None:
            self.overfire_threshold = overfire_threshold

    def reset_threshold(self) -> None:
        self.creosote_threshold = CREOSOTE_THRESHOLD
        self.overfire_threshold = OVERFIRE_THRESHOLD

    def get_sensor_data(self) -> int:
        return 1

    def update_led_state(self) -> None:
        temperature = self.get_sensor_data()
        new_state = self.led_states

        if temperature >= self.alarm_threshold:
            new_state = (True, True, True, True, True, True, True)

        elif temperature >= self.overfire_threshold:
            new_state = (True, True, True, True, True, True, False)

        elif temperature >= OPTIMAL_LED_3_THRESHOLD_RATIO * self.overfire_threshold:
            new_state = (True, True, True, True, True, False, False)

        elif temperature >= OPTIMAL_LED_2_THRESHOLD_RATIO * (
            self.creosote_threshold + self.overfire_threshold
        ):
            new_state = (True, True, True, True, False, False, False)

        elif temperature >= self.creosote_threshold:
            new_state = (True, True, True, False, False, False, False)

        elif CREOSOTE_LED_2_THRESHOLD_RATIO < temperature < self.creosote_threshold:
            new_state = (True, True, False, False, False, False, False)

        else:
            new_state = BASE_LED_STATE

        if new_state != self.led_states:
            self.led_states = new_state
            for led, state in enumerate(new_state):
                self.set_led(led, state)

    def is_connected(self) -> bool:
        return True

    def set_led(self, led: int, state: bool) -> None:
        pass

    def not_connected_led_mode(self) -> None:
        while not self.is_connected():
            for i, state in enumerate(self.led_states):
                if state:
                    self.set_led(i, state)
                    sleep(0.2)