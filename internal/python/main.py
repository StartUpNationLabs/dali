from chaining import create_app_with_name

(create_app_with_name("testApp")
    .with_buzzer_with_name("buzzer").on_pin(1)
    .with_sensor_with_name("button").on_pin(2)
    .with_digital_actuator_with_name("led").on_pin(3)
    .with_initial_state_with_name("state1")
        .add_transition_to("state2")
            .when_the_sensor_with_name("button").go_from_high_to_low
                .and_condition("button").have_high_value
                .end_transition
            .switch_on_digital_actuator_with_name("led")
        .end_state
    .with_state_with_name("state2")
        .switch_off_digital_actuator_with_name("led")
        .play_music_with_buzzer_named("buzzer")
            .at_frequency(32)
            .during(15)
            .end_melody
        .end_state
    .build)