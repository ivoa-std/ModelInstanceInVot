from mapping_factory import logger

class VodmlConstraint:    
    def __init__(self, att_role, subset, description):
        self._att_role = att_role
        self._subset = subset
        self._description = description
        
    def __str__(self):
        retour =  "CONSTRAINT "
        retour += self._att_role + "=>" + self._subset + "(" + self.description + ")"
        return retour
             
    def __repr__(self):
        return self.__str__()
    
    @property
    def att_role(self):
        return self._att_role
    
    @property
    def subset(self):
        return self._subset
    @property
    def description(self):
        return self._description
    
    @property
    def is_subset(self):
        return True if self._subset and self._att_role  else False
    

    
class VodmlConstraintDict:    
    def __init__(self):
        self._constraints = dict()
        
    def __str__(self):
        retour =  "CONSTRAINTS [ "
        for r, vc in self._constraints.items():
            retour += r + ": " + vc.__str__() + " "
        retour += "]"
        return retour
    
    def __repr__(self):
        return self.__str__()
    
    def add_contraint(self, vodml_contraint):
        if vodml_contraint.att_role == "coords:Coordinate.frame":
            logger.error("======== constraint already here")
        if vodml_contraint.is_subset:
            self._constraints[vodml_contraint.att_role] = vodml_contraint
        else:
            self._constraints["NoSubset"] = vodml_contraint
    
    @property
    def constraints(self):
        return self._constraints
    
    def get_constraint(self, key):
        if key in self._constraints.keys():
            return self._constraints[key]
        else:
            return None
        
    def get_nosubset_constraint(self):
        return self.get_constraint("NoSubset")
        
    def items(self):
        return self._constraints.items()
    
    def keys(self):
        return self._constraints.keys()
    
    def merge(self, vodml_constraint_dict):
        for k, vodml_constraint in vodml_constraint_dict.constraints.items():
            if k not in self._constraints.keys():
                self._constraints[k] = vodml_constraint
            else:
                self.add_contraint(vodml_constraint)
        