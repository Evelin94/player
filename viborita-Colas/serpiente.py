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
        self.snake_direction = "Right"
        self.food = None
        self.create_food()
        self.game_running = True
        
        # Llamamos a la funcion de movimiento cada 100 ms
        self.window.after(100, self.move_snake)
        
        # Capturamos las teclas para mover la serpiente
        self.window.bind("<KeyPress>", self.change_direction)

    def create_food(self):
        # Generar la comida en una posicion aleatoria
        food_x = random.randint(0, (self.width - 10) // 10) * 10
        food_y = random.randint(0, (self.height - 10) // 10) * 10
        self.food = (food_x, food_y)
        self.canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill="red", tags="food")
        
    def draw_snake(self):
        self.canvas.delete("snake") 
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green", tags="snake")
    
    def move_snake(self):
        if not self.game_running:
            return

        head_x, head_y = self.snake[0]

        # Cambiar la posición de la cabeza de la serpiente según la direccion
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

        # Verificar si la serpiente comio la comida
        if new_head == self.food:
            self.snake.append(self.snake[-1])  # Alargar la serpiente
            self.create_food()  # Crear nueva comida

        # Verificar si la serpiente choca contra sii misma o las paredes
        if (head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height or
            new_head in self.snake[1:]):
            self.game_running = False
            self.canvas.create_text(self.width // 2, self.height // 2, text="¡GAME OVER!", fill="white", font=("Arial", 24))

        self.draw_snake()  # Redibujar la serpiente
        self.window.after(100, self.move_snake)  # Llamar a la funcion despues de 100 ms
    
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


'''import curses  # Para la interfaz de terminal en juegos simples
import random

def iniciar_juego():
    try:
        pantalla = curses.initscr()
        curses.curs_set(0)
        altura, ancho = 20, 60
        ventana = curses.newwin(altura, ancho, 0, 0)
        ventana.keypad(1)
        ventana.timeout(100)

        serpiente_x = ancho // 4
        serpiente_y = altura // 2
        serpiente = [(serpiente_y, serpiente_x), (serpiente_y, serpiente_x - 1), (serpiente_y, serpiente_x - 2)]

        comida = (random.randint(1, altura - 2), random.randint(1, ancho - 2))
        ventana.addch(comida[0], comida[1], '*')

        tecla = curses.KEY_RIGHT
        puntaje = 0

        while True:
            siguiente_tecla = ventana.getch()
            tecla = tecla if siguiente_tecla == -1 else siguiente_tecla

            # Calcular nueva posición de la cabeza
            if tecla == curses.KEY_DOWN:
                nueva_cabeza = (serpiente[0][0] + 1, serpiente[0][1])
            elif tecla == curses.KEY_UP:
                nueva_cabeza = (serpiente[0][0] - 1, serpiente[0][1])
            elif tecla == curses.KEY_LEFT:
                nueva_cabeza = (serpiente[0][0], serpiente[0][1] - 1)
            elif tecla == curses.KEY_RIGHT:
                nueva_cabeza = (serpiente[0][0], serpiente[0][1] + 1)

            # Verificar colisiones
            if (nueva_cabeza[0] in [0, altura] or
                nueva_cabeza[1] in [0, ancho] or
                nueva_cabeza in serpiente):
                curses.endwin()
                print("Juego terminado. Puntaje:", puntaje)
                break

            # Insertar la nueva cabeza en la serpiente
            serpiente.insert(0, nueva_cabeza)

            # Si la serpiente come la comida
            if serpiente[0] == comida:
                puntaje += 1
                comida = None
                while comida is None:
                    nueva_comida = (
                        random.randint(1, altura - 2),
                        random.randint(1, ancho - 2)
                    )
                    comida = nueva_comida if nueva_comida not in serpiente else None
                ventana.addch(comida[0], comida[1], '*')
            else:
                # Mover la serpiente eliminando el último segmento
                cola = serpiente.pop()
                ventana.addch(cola[0], cola[1], ' ')

            # Mostrar la serpiente en pantalla
            ventana.addch(serpiente[0][0], serpiente[0][1], '#')

    except Exception as e:
        curses.endwin()
        print("Ocurrió un error:", e)

# Ejecutar el juego
iniciar_juego()
'''