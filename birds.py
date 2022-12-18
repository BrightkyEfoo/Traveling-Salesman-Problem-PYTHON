class Bird:
    """Un oiseau. 🐦"""

    # ici on utilise deux attributs de classe.
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, name):
        """Les attributs définis ici sont des attributs d'instance."""
        self.position = 1, 2
        self.name = name
        
        # On accède à l'attribut de classe "positions" avec self (c'est possible).
        self.positions[self.position] = self.name

    @classmethod
    def find_bird(cls, position):
        """Retrouve un oiseau selon la position donnée."""
        print(f'position : {position}')
        if position in cls.positions:
            return f"On a trouvé \"{cls.positions[position]}\" !"

        return "On a rien trouvé..."


# On peut accéder aux variables de classe sans instanciation.
Bird.names
print(f"Bird.positions :{Bird.positions}")
print(Bird.find_bird((2, 5)))

# On instancie un oiseau
bird = Bird("mouette")
print(f"Bird.positions :{Bird.positions}")
# On le retrouve avec la méthode find_bird.
print(Bird.find_bird((1, 2)))