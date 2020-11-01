                           ****** CHALLENGE ******

Develop a multi-thread Python application to fetch, analyse and store data.
The application should have a threadpool (or a set of threadpools) of two different kinds of components:
- The first component should be in charge of fetching the data from a "source" entity, and store it in a message queue
- The second component should be in charge of working on the same queue, by performing some operations on each item through a "processing" entity, and finally sending it to a "destination" entity
The development of the "source", "processing" and "destination" entities is not in the scope of this exercise, so it's up to you to abstract or mock them accordingly.

Tips:
- Ensure access to shared resources is thread-safe
- If you lack of fantasy, you can just use some input JSON objects and "process" them by altering their properties
- Assume the code would eventually need to be extended to support additional sources, destinations or processing entities, so abstract common data structures and/or routines when possible
- Unit/integration tests are more than welcome
- Keep it simple... don't overshoot

Deadline: 2 days

                            ****** SOLUTION ******

For this challenge I propose a solution structured as follows:

1. A producer/consumer architecture implemented with a threadpool with a configurable number of workers, buffer size.

    This implementation can be used in two ways, the first allows a free flow of data production and consumption and a second option to produce and consume a limited amount of data.
also has a sentinel implementation that is responsible for tracing the events produced and consumed, also collects an example of the data processed and control the access to the buffer (queue)

    *All this implementation is in the "core" module*

2. An *"Factory Object"* designer pattern was implemented in the following modules: *source, target and process*, the objective of this implementation is to allow different entities to be added easily without altering the communication interfaces of the main program

3. This application can be used in two ways: 
 - Produce and consume freely an unlimited amount of events (limited only by the runtime configured in the shutdown_time variable found in settings.py)
    
    *dispatcher.dispatch()* 
 - Produce a fixed number of events to be consumed, this allows block processing (limited by the defined buffer size)
 
    *number_events=2000*
 
    *dispatcher.dispatch(number_events)* 

                        ****** USE OF THE APPLICATION ******
                       
Using python 3.7                       
1. install pipenv : https://pypi.org/project/pipenv/

2. install the libraries specified in the pipfile:
    
    *pipenv install*

3. Run the main program 
    
    *python main.py*
    
This file is located in multithread_challenge/main.py

4. Run the tests (inside multithread_challenge folder):

    *pytest -ra -vv -l -p no:warnings  --gherkin-terminal-reporter --gherkin-terminal-reporter-expanded*




