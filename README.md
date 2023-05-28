# N-Design Patterns In One Python Project
This python project, **SmartHomeSystem**, shows the usage of 21 design patterns:

-   Creational Patterns:
    
    -   **Abstract Factory:** Create families of related objects like a set of "Smart Devices" (e.g., Smart Light, Smart Lock, etc).
    -   **Builder:** Configure complex objects step by step, like a RoomBuilder to create different types of rooms with different devices.
    -   **Factory Method:** Define an interface for creating objects, but let subclasses decide which class to instantiate.
    -   **Prototype:** Clone a pre-configured device, like a standard configured light, instead of creating a new one from scratch.
    -   **Singleton:** Have a single "Home" object that coordinates and manages all operations in the system.
-   Structural Patterns:
    
    -   **Adapter:** Enable classes with incompatible interfaces to collaborate. A 'Smart Device' adapter that allows legacy devices to be controlled.
    -   **Bridge:** Decouple an abstraction from its implementation so the two can vary independently.
    -   **Composite:** Compose objects into tree structures to represent part-whole hierarchies.
    -   **Decorator:** Add responsibilities to objects dynamically by wrapping them with a decorator class.
    -   **Facade:** Simplify complex system interactions with a unified high-level interface.
    -   **Flyweight:** Use sharing to support large numbers of fine-grained objects efficiently.
    -   **Proxy:** Provide a surrogate or placeholder for another object to control access to it, like a proxy for the network communication.
-   Behavioral Patterns:
    
    -   **Chain of Responsibility:** Create a chain of receiver objects for a request, like a sequence of checks before an action (security checks, power-saving checks, etc.)
    -   **Command:** Encapsulate a request as an object to allow parameterizing clients with queues, requests, and operations.
    -   **Interpreter:** Implement a language interpreter for a small language like a 'Smart Device' programming language.
    -   **Iterator:** Access the elements of an aggregate object sequentially without exposing its underlying representation.
    -   **Memento:** Capture and externalize an object's internal state without violating encapsulation.
    -   **Observer:** Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
    -   **State:** Allow an object to alter its behavior when its internal state changes.
    -   **Strategy:** Define a family of algorithms, encapsulate each one, and make them interchangeable. Like power management strategies for various devices.
    
    -   **Visitor:** Represent an operation to be performed on the elements of an object structure. Visitors can perform operations across a set of different classes. 


The following two patterns are not used. Share some good idea with me!
-   **Template Method:** Define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
-   **Mediator:** Define an object that encapsulates how a set of objects interact, like a `SmartHubMediator`.  
