# solar_sandbox.py
# Module 2 Sandbox — "How does Pygame display things?"
# Goal: Open a window and draw a simple solar system (sun + planets).

import math
import pygame

# ---------------------------
# SETTINGS (easy knobs)
# ---------------------------
WIDTH, HEIGHT = 900, 520
FPS = 60

# Colors (R, G, B)
SPACE = (5, 8, 20)
WHITE = (240, 240, 240)
SUN = (255, 190, 60)

# ---------------------------
# PLANET DATA (Module 0 style: simple variables)
# Each planet is a dictionary. We'll draw each one.
# ---------------------------
planets = [
    {"name": "Mercury", "radius": 6,  "orbit": 60,  "speed": 1.8, "color": (170, 170, 170), "angle": 0.0},
    {"name": "Venus",   "radius": 9,  "orbit": 95,  "speed": 1.3, "color": (220, 190, 120), "angle": 0.0},
    {"name": "Earth",   "radius": 10, "orbit": 130, "speed": 1.0, "color": (90, 160, 255),  "angle": 0.0},
    {"name": "Mars",    "radius": 8,  "orbit": 165, "speed": 0.85,"color": (230, 120, 90),  "angle": 0.0},
]

# TODO 1 (Student): Add one more planet:
# Example:
# {"name": "Jupiter", "radius": 16, "orbit": 220, "speed": 0.55, "color": (210, 170, 120), "angle": 0.0}

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Solar Sandbox — Pygame Display Demo")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("consolas", 18)
    small = pygame.font.SysFont("consolas", 14)

    # Center of our solar system
    cx, cy = WIDTH // 2, HEIGHT // 2

    running = True
    paused = False

    while running:
        dt = clock.tick(FPS) / 1000.0  # seconds since last frame

        # ---------------------------
        # EVENTS (keyboard / quit)
        # ---------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    paused = not paused

        # ---------------------------
        # UPDATE (math / movement)
        # ---------------------------
        if not paused:
            for p in planets:
                # We update the angle every frame.
                # speed is "radians per second" (smaller = slower orbit)
                p["angle"] += p["speed"] * dt

        # ---------------------------
        # DRAW (this is what makes it visible)
        # ---------------------------
        screen.fill(SPACE)

        # Draw orbit rings
        for p in planets:
            pygame.draw.circle(screen, (40, 55, 90), (cx, cy), p["orbit"], width=1)

        # Draw the sun
        pygame.draw.circle(screen, SUN, (cx, cy), 22)
        pygame.draw.circle(screen, (255, 240, 200), (cx, cy), 22, width=2)

        # Draw each planet at its orbit position
        for p in planets:
            x = cx + int(math.cos(p["angle"]) * p["orbit"])
            y = cy + int(math.sin(p["angle"]) * p["orbit"])
            pygame.draw.circle(screen, p["color"], (x, y), p["radius"])
            pygame.draw.circle(screen, WHITE, (x, y), p["radius"], width=1)

            # Optional label (comment out if too busy)
            label = small.render(p["name"], True, (180, 190, 220))
            screen.blit(label, (x + p["radius"] + 6, y - 8))

        # HUD text
        title = font.render("Solar Sandbox", True, (230, 230, 240))
        screen.blit(title, (16, 14))

        instr = small.render("ESC quit | SPACE pause/unpause | TODO: add a planet", True, (170, 180, 200))
        screen.blit(instr, (16, 40))

        # TODO 2 (Student): Print the number of planets on screen:
        # Example: "Planets: 4"
        count_text = small.render(f"Planets: {len(planets)}", True, (170, 180, 200))
        screen.blit(count_text, (16, 60))

        # TODO 3 (Student): Add a starfield background (5-20 dots)
        # Hint: use pygame.draw.circle inside a loop with random positions.
        # Keep it simple: draw the SAME stars every frame by pre-making a stars list.

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
