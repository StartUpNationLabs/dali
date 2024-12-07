from chaining import create_app

(create_app("testApp")
    .with_buzzer("buzzer").on_pin(1)
    .with_sensor("button").on_pin(2)
    .with_digital_actuator("led").on_pin(3)
    .with_initial_state("state1")
        .switch_on("buzzer")
        .add_transition_to("state2")
            .when("button").go_from_low_to_high
                .and_("button").does_not.have_low_value
                .end_transition
        .end_state
    .with_state("state2")
        .switch_off("led")
        .play_music_with_buzzer("buzzer", 32)
            .during(15)
            .end_melody
        .end_state
    .build)