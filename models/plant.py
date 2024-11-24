class Plant:
  scientific_name: str
  id_algorithm:int
  name:str
  description:str
  family:str
  origin:str
  tipo: str
  added_date:str
  
  
  def __init__ (self,
                scientific_name: str,
                id_algorithm:int,
                name:str,
                description:str,
                family:str,
                origin:str,
                tipo: str,
                added_date:str
            ):
    self.scientific_name = scientific_name
    self.id_algorithm = id_algorithm
    self.name = name
    self.description = description
    self.family = family
    self.origin = origin
    self.tipo = tipo
    self.added_date = added_date 
