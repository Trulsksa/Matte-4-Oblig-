import numpy as np
import matplotlib.pyplot as plt



def Varmelikningen_2D(L, T, N, alpha, u_t0):
    h = L / N  # gitterlengden i x og y-retning
    
    dt = 0.5 * h**2   # k/h^2 = 1/2 --> innenfor kravet 
    Nt = int(T / dt)  # Justere antall tidssteg basert på dt 
    
    x = np.linspace(0, L, N + 1)
    y = np.linspace(0, L, N + 1)
    X, Y = np.meshgrid(x, y) 
    
    u = np.zeros((N + 1, N + 1)) 
    u_ny = np.zeros((N + 1, N + 1))
    u[:, :] = u_t0(X, Y)
    
    for _ in range(Nt): 
        u_ny[1:-1, 1:-1] = u[1:-1, 1:-1]  +  alpha * (dt / h**2) * ((u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1])   +   (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]))

        u[:, :] = u_ny[:, :]
        
    return X, Y, u


# Velger en startilstand for varmelinkingen i t = 0
def u_t0(x, y):
    return np.sin( 2 * np.pi * x)

# Parametere
L = 1.0      # total lengde i x og y retning 
T = 0.1     # Økt T for å vise løsningen ved ulike tider
N = 40       # antall ruter i en ratning --> 40 * 40 grid = 1600 tiles 
alpha = 0.07 # termiske diffusiviteten justert for å få utgjvningsprosessen til 1 sekund

# Løser likningen
X, Y, u = Varmelikningen_2D(L, T, N, alpha, u_t0)

# Oppretter en figur og en 3D akse for plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, u, cmap='viridis', vmin=-1, vmax=1)
ax.set_zlim(-1, 1)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u(x, y, T)')
ax.set_title('3D-plot av løsningen på varmelikningen i 2D ved T = {:.2f} med fast U-akse og fargeskala fra -1 til 1'.format(T))


plt.show()
