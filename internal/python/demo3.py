from chaining import create_app

(create_app("demo-3")
    .with_sensor("button").on_pin(1)
    .with_buzzer("buzzer").on_pin(2)
    
    .with_initial_state("stateOff")
        .switch_off("buzzer")
        .add_transition_to("stateOn")
        # If a button go from low to high, it's an edge detection that allow us to detect a distinct button click
            .when("button").go_from_low_to_high
                .end_transition
        .end_state
        
    .with_state("stateOn")
        .switch_on("buzzer")
        .add_transition_to("stateOff")
        # If a button go from low to high, it's an edge detection that allow us to detect a distinct button click
            .when("button").go_from_low_to_high 
                .end_transition
        .end_state
        
    .build)