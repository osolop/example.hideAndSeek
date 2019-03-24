# hideAndSeek game

This is a capsule submission for the SRPOL Bixby Hackathon.

The capsule is called "Hide & Seek" and it is simple voice controll game.

The game depends on seeking the hidden object. Player allowed to move on the map and check hidden places.

The capsule uses Bixby for natural language processing and an external RESTful web api written in Python for calculations and memory.

This repo contains both the capsule, the web api and two user stories used for end-to-end testing of the capsule.

The NLP part of the system is mostly feature-complete. Perhaps an additional parameter for the volume of consumed beverages could be implemented and a more complex transactional model could be used in addition to the simple single-utterance commit that is currently available.

The server side part of the system is very rudimentary and should be completely overhauled in case of any comercial system. It was designed with the limitations of the free version of the hosting service pythonanywhere.com in mind.
