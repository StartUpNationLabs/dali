from chaining import create_app

(create_app("demo-1")
    .with_sensor("button").on_pin(1)
    .with_buzzer("buzzer").on_pin(2)
    .with_digital_actuator("led").on_pin(3)
    
    .with_initial_state("stateOff")
        .switch_off("buzzer")
        .switch_off("led")
        .add_transition_to("stateOn")
            .when("button").have_high_value
                .end_transition
        .end_state
        
    .with_state("stateOn")
        .switch_on("buzzer")
        .switch_on("led")
        .add_transition_to("stateOff")
            .when("button").have_low_value
                .end_transition
        .end_state
    .build)