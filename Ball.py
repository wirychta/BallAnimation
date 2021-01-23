# Program na zaliczenie ćwiczeń z fizyki o nazwie "Animacja odbijającej się piłki"
# by Wiktor Rychta
# nr albumu: 10951
# Program wykorzystuje bibliotekę Matplotlib, którą trzeba doinstalować aby program wyświtlił sie prawidłowo.
# Poniższy program animuje odbijającą się piłkę, zaczynając od pozycji (0, y0) (0, y0) z prędkością (vx0,0) (vx0,0).
# Pozycja piłki, historia trajektorii i wysokość zmieniają się z każdą wyświetlaną klatką.
# 22.01.2021




import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Przyspiesznie ziemskie, m.s-2.
g = 9.81
# Maksymalny zakres trajektorii pilki do wykreslenia.
XMAX = 6
# Wspolczynnik restytucji od odbicia (-v_w górę / v_w dół).
cor = 0.65
# Czas animacji.
dt = 0.005

# Poczatkowe wektory polozenia i predkosci
x0, y0 = 0, 4
vx0, vy0 = 1, 0



def get_pos(t=0):

    """Generator określajacy pozycje pilki w czasie t."""
    x, y, vx, vy = x0, y0, vx0, vy0
    while x < XMAX:
        t += dt
        x += vx0 * dt
        y += vy * dt
        vy -= g * dt
        if y < 0:
            # Odbicie
            y = 0
            vy = -vy * cor
        yield x, y


def init():
    """Zainicjuj figurę animacji."""
    ax.set_xlim(0, XMAX)
    ax.set_ylim(0, y0)
    ax.set_xlabel('$x$ /m')
    ax.set_ylabel('$y$ /m')
    line.set_data(xdata, ydata)
    ball.set_center((x0, y0))
    height_text.set_text(f'Wysokość: {y0:.1f} m')
    return line, ball, height_text


def animate(pos):
    """Dla każdej klatki przesuń animację do nowej pozycji, pos."""
    x, y = pos
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    ball.set_center((x, y))
    height_text.set_text(f'Wysokość: {y:.1f} m')
    return line, ball, height_text

# Skonfiguruj nową figurę o równych proporcjach, aby kula wyglądała na okrągłą.
fig, ax = plt.subplots()
ax.set_aspect('equal')

# To są obiekty, które musimy śledzić.
line, = ax.plot([], [], lw=2)
ball = plt.Circle((x0, y0), 0.08)
height_text = ax.text(XMAX*0.5, y0*0.8, f'Wysokość: {y0:.1f} m')
ax.add_patch(ball)
xdata, ydata = [], []

interval = 1000*dt
ani = animation.FuncAnimation(fig, animate, get_pos, blit=True,
                      interval=interval, repeat=False, init_func=init)
plt.show()
