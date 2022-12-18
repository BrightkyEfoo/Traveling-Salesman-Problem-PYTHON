class ToolBox:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enleve un outil."""
        index = self.tools.index(tool)
        del self.tools[index]

 

class Screwdriver:
    """Tournevis."""

    def __init__(self, size=3):
        """Initialise la taille."""
        self.size = size
    
    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()
    
    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()
    
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"


class Hammer:
    """Marteau."""

    def __init__(self, color="red"):
        """Initialise la couleur."""
        self.color = color
    
    def paint(self, color):
        """Paint le marteau."""
        self.color = color
    
    def hammer_in(self, nail):
        """Enfonce un clou."""
        nail.nail_in()
    
    def remove(self, nail):
        """Enleve un clou."""
        nail.remove()
    
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Marteau de couleur {self.color}"


class Screw:
    """Vis."""
     
    MAX_TIGHTNESS = 5
    
    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0
    
    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1
    
    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1
    
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""
    
    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False
    
    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True
    
    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False
    
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."

boite = ToolBox()
tournevis = Screwdriver(4)
marteau = Hammer("black")
boite.add_tool(tournevis)
boite.add_tool(marteau)
visse = Screw()
tournevis.tighten(visse)
print(visse)