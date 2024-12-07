from chaining import create_app

# The rest of the music was not added here due to linting issue due to the number of chained called it involved in python, but it was only a linting issue not a functional one

(create_app("demo-music")
    .with_sensor("button").on_pin(1)
    .with_buzzer("buzzer").on_pin(3)
    
    .with_initial_state("stateIdle")
        .switch_off("buzzer")
        .add_transition_to("stateMusic")
            .when("button").have_high_value
                .end_transition
                
        .end_state
        
    .with_state("stateMusic")
        .play_music_with_buzzer("buzzer", 330).during(400).end_melody
        .play_music_with_buzzer("buzzer", 0).during(100).end_melody
        .play_music_with_buzzer("buzzer", 330).during(400).end_melody
        .play_music_with_buzzer("buzzer", 0).during(100).end_melody
        .play_music_with_buzzer("buzzer", 330).during(800).end_melody
        .play_music_with_buzzer("buzzer", 0).during(200).end_melody
        .play_music_with_buzzer("buzzer", 330).during(400).end_melody
        .play_music_with_buzzer("buzzer", 0).during(100).end_melody
        .play_music_with_buzzer("buzzer", 330).during(400).end_melody
        .play_music_with_buzzer("buzzer", 0).during(100).end_melody
        .play_music_with_buzzer("buzzer", 330).during(800).end_melody
        .play_music_with_buzzer("buzzer", 0).during(200).end_melody
        .play_music_with_buzzer("buzzer", 330).during(400).end_melody
        .play_music_with_buzzer("buzzer", 0).during(100).end_melody
        .play_music_with_buzzer("buzzer", 392).during(400).end_melody
        .play_music_with_buzzer("buzzer", 0).during(100).end_melody
        .play_music_with_buzzer("buzzer", 262).during(400).end_melody
        .play_music_with_buzzer("buzzer", 0).during(100).end_melody
        .play_music_with_buzzer("buzzer", 294).during(400).end_melody
        .play_music_with_buzzer("buzzer", 0).during(100).end_melody
        .play_music_with_buzzer("buzzer", 330).during(1600).end_melody
        .play_music_with_buzzer("buzzer", 0).during(400).end_melody
        .add_transition_to("stateIdle").when_actions_are_finished
        .end_state
        
    .build)