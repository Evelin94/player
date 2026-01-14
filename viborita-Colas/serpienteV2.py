import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
       
        self.window = tk.Tk()
        self.window.title("Viborita (Snake)")
        
        self.width = 600
        self.height = 400
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg="black")
        self.canvas.pack()
        
        self.snake = [(100, 100), (90, 100), (80, 100)]  # Coordenadas de la serpiente
        self.snake_direction = "Right"
        self.foods = []  # Lista para manejar multiples comidas (posicion y color)
        self.game_running = True
        
        self.target_red_count = 5  #  bloques rojos
        self.target_green_count = 3  #  bloques verdes
        
        self.create_foods()  # Crear comida inicial
        
        # Llamamos a la función de movimiento cada 100 ms
        self.window.after(100, self.move_snake)
        
        #  teclas para mover la serpiente
        self.window.bind("<KeyPress>", self.change_direction)

    def create_foods(self):
        # Contar comidas existentes por color
        current_red_count = len([f for f in self.foods if f[2] == "red"])
        current_green_count = len([f for f in self.foods if f[2] == "green"])
        
        # Generar bloques hasta alcanzar los objetivos de cada color
        while current_red_count < self.target_red_count or current_green_count < self.target_green_count:
            food_x = random.randint(0, (self.width - 10) // 10) * 10
            food_y = random.randint(0, (self.height - 10) // 10) * 10
            
            # Asegurar que no se cree comida en la posición de la serpiente o en otra comida
            if (food_x, food_y) in [segment[:2] for segment in self.snake] or \
               (food_x, food_y) in [(food[0], food[1]) for food in self.foods]:
                continue
            
            food_color = "red" if current_red_count < self.target_red_count else "green"
            
            self.foods.append((food_x, food_y, food_color))
            self.canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill=food_color, tags=f"food_{food_color}")
            
            # Actualizar conteos
            if food_color == "red":
                current_red_count += 1
            else:
                current_green_count += 1
        
    def draw_snake(self):
        self.canvas.delete("snake")  # Borra la serpiente antes de redibujarla
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green", tags="snake")
    
    def move_snake(self):
        if not self.game_running:
            return

        head_x, head_y = self.snake[0]

        # Cambiar la posicion de la cabeza de la serpiente según la direccion
        if self.snake_direction == "Right":
            head_x += 10
        elif self.snake_direction == "Left":
            head_x -= 10
        elif self.snake_direction == "Up":
            head_y -= 10
        elif self.snake_direction == "Down":
            head_y += 10

        # Añadir la nueva cabeza de la serpiente
        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

        # Verificar si la serpiente comio alguna comida
        for food in self.foods:
            if new_head == (food[0], food[1]):
                if food[2] == "green":
                    # Añadir un segmento si la comida es verde
                    self.snake.append(self.snake[-1])
                elif food[2] == "red" and len(self.snake) > 1:
                    # Quitar un segmento si la comida es roja
                    self.snake.pop()
                
                # Eliminar la comida consumida
                self.foods.remove(food)
                self.canvas.delete(f"food_{food[2]}")
                break
        
        # Verificar y mantener el balance de comidas
        self.create_foods()

        # Verificar si la serpiente choca contra sí misma o las paredes
        if (head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height or
            new_head in self.snake[1:]):
            self.game_running = False
            self.canvas.create_text(self.width // 2, self.height // 2, text="¡GAME OVER!", fill="white", font=("Arial", 24))

        self.draw_snake()  # Redibujar la serpiente
        self.window.after(100, self.move_snake)  # Llamar a la función despuée de 100 ms
    
    def change_direction(self, event):
        if event.keysym == "Right" and self.snake_direction != "Left":
            self.snake_direction = "Right"
        elif event.keysym == "Left" and self.snake_direction != "Right":
            self.snake_direction = "Left"
        elif event.keysym == "Up" and self.snake_direction != "Down":
            self.snake_direction = "Up"
        elif event.keysym == "Down" and self.snake_direction != "Up":
            self.snake_direction = "Down"

    def run(self):
        self.window.mainloop()

# Crear una instancia del juego y ejecutarlo
if __name__ == "__main__":
    game = SnakeGame()
    game.run()
