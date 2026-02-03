#!/usr/bin/python3
"""Abstract class Animal and subclasses Dog/Cat"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class"""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal"""
        pass


class Dog(Animal):
    """Dog class"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class"""

    def sound(self):
        return "Meow"
