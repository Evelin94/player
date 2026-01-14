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

       
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_numbers = [1, 2, 3]  
        self.snake_direction = "Right"
        self.foods = []  
        self.food_colors = ["red", "green"]
        self.game_running = True

        self.target_red_count = 3
        self.target_green_count = 2

        self.create_foods()
        self.window.after(100, self.move_snake)
        self.window.bind("<KeyPress>", self.change_direction)

    def create_foods(self):
        
        current_red = len([f for f in self.foods if f[2] == "red"])
        current_green = len([f for f in self.foods if f[2] == "green"])

        while current_red < self.target_red_count or current_green < self.target_green_count:
            food_x = random.randint(0, (self.width - 10) // 10) * 10
            food_y = random.randint(0, (self.height - 10) // 10) * 10

            if (food_x, food_y) in [segment for segment in self.snake] or \
               (food_x, food_y) in [(f[0], f[1]) for f in self.foods]:
                continue

            food_color = "red" if current_red < self.target_red_count else "green"
            self.foods.append((food_x, food_y, food_color))
            self.canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill=food_color, tags=f"food_{food_color}")

            if food_color == "red":
                current_red += 1
            else:
                current_green += 1

    def draw_snake(self):
        self.canvas.delete("snake")
        for index, segment in enumerate(self.snake):
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tags="snake")
            self.canvas.create_text(x + 5, y + 5, text=str(self.snake_numbers[index]), fill="white", tags="snake")

    def move_snake(self):
        if not self.game_running:
            return

        head_x, head_y = self.snake[0]

        if self.snake_direction == "Right":
            head_x += 10
        elif self.snake_direction == "Left":
            head_x -= 10
        elif self.snake_direction == "Up":
            head_y -= 10
        elif self.snake_direction == "Down":
            head_y += 10

        new_head = (head_x, head_y)

        if new_head in self.snake or head_x < 0 or head_y < 0 or head_x >= self.width or head_y >= self.height:
            self.game_running = False
            self.canvas.create_text(self.width // 2, self.height // 2, text="¡GAME OVER!", fill="white", font=("Arial", 24))
            return

        # Cmprobr si la cabeza est sobre una comida
        for food in self.foods:
            if new_head == (food[0], food[1]):
                if food[2] == "green":
                   
                    self.snake.append(self.snake[-1])
                    self.snake_numbers.append(self.snake_numbers[-1] + 1)
                elif food[2] == "red" and len(self.snake) > 1:
                    
                    self.snake.pop(0)
                    self.snake_numbers.pop(0)

                self.foods.remove(food)
                self.canvas.delete(f"food_{food[2]}")
                break

        self.snake = [new_head] + self.snake[:-1]
        self.draw_snake()
        self.create_foods()

        self.window.after(100, self.move_snake)

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


if __name__ == "__main__":
    game = SnakeGame()
    game.run()

