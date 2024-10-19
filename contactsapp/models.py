import random
import hashlib
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    def initial_color(self):
        colors = {

            'A': ['#380303', '#071E42', '#1B053D', '#3B0537', '#03034E', '#470911', '#012F0D'],  # Multiple colors for A
            'B': ['#33CC33', '#228B22', '#00FF7F', '#FF69B4', '#FF1493', '#FFB6C1'],  # Multiple colors for B
            'C': ['#6666CC', '#8A2BE2', '#7B68EE'],  # Multiple colors for C
            'D': ['#CC3333', '#DC143C', '#FF6347'],  # Multiple colors for D
            'E': ['#33CCCC', '#20B2AA', '#48D1CC'],  # Multiple colors for E
            'F': ['#CC66CC', '#DA70D6', '#DDA0DD'],  # Multiple colors for F
            'G': ['#66CCCC', '#5F9EA0', '#4682B4'],  # Multiple colors for G
            'H': ['#CCCC33', '#FFD700', '#FFFF00'],  # Multiple colors for H
            'I': ['#CC9966', '#B8860B', '#CD853F'],  # Multiple colors for I
            'J': ['#33CC66', '#3CB371', '#32CD32'],  # Multiple colors for J
            'K': ['#6666CC', '#7B68EE', '#8470FF'],  # Multiple colors for K
            'L': ['#CC33CC', '#FF00FF', '#FF1493'],  # Multiple colors for L
            'M': ['#33CCCC', '#00CED1', '#40E0D0'],  # Multiple colors for M
            'N': ['#CC6666', '#FF7F50', '#CD5C5C'],  # Multiple colors for N
            'O': ['#66CCCC', '#1E90FF', '#00BFFF'],  # Multiple colors for O
            'P': ['#CCCC33', '#FFD700', '#FFFACD'],  # Multiple colors for P
            'Q': ['#CC9966', '#B22222', '#CD853F'],  # Multiple colors for Q
            'R': ['#33CC66', '#2E8B57', '#3CB371'],  # Multiple colors for R
            'S': ['#6666CC', '#6A5ACD', '#4682B4'],  # Multiple colors for S
            'T': ['#CC33CC', '#DA70D6', '#DDA0DD'],  # Multiple colors for T
            'U': ['#33CCCC', '#00BFFF', '#48D1CC'],  # Multiple colors for U
            'V': ['#CC6666', '#CD5C5C', '#FF6347'],  # Multiple colors for V
            'W': ['#66CCCC', '#20B2AA', '#3CB371'],  # Multiple colors for W
            'X': ['#CCCC33', '#FFD700', '#FFFF00'],  # Multiple colors for X
            'Y': ['#CC9966', '#B8860B', '#DAA520'],  # Multiple colors for Y
            'Z': ['#33CC66', '#32CD32', '#3CB371']   # Multiple colors for Z
            
            
            
        }
        #return colors.get(self.first_name[0].upper(), '#CCCCCC') 
        if not self.first_name:
            return ['#CCCCCC']  

        initial = self.first_name[0].upper()
        color_list = colors.get(initial, ['#CCCCCC'])  

        chosen_color = random.choice(color_list)
        return chosen_color 
    


     