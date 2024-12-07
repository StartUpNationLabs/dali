from chaining import create_app

(create_app("demo-2")
    .with_sensor("button1").on_pin(1)
    .with_sensor("button2").on_pin(2)
    .with_buzzer("buzzer").on_pin(3)
    
    .with_initial_state("stateOff")
        .switch_off("buzzer")
        .add_transition_to("stateOn")
            .when("button1").have_high_value
            .and_("button2").have_high_value
                .end_transition
        .end_state
        
    .with_state("stateOn")
        .switch_on("buzzer")
        .add_transition_to("stateOff")
            .when("button1").have_low_value
            .or_("button2").have_low_value
                .end_transition
        .end_state
        
    .build)