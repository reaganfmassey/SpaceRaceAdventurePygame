
# Space Adventure Game (Module 2) — Student Reference + Deliverables

## Goal
You will build a **Pygame “Solar System Sandbox”** to prove you can:
- open a window reliably
- draw objects (planets/stars)
- move things using variables + conditionals
- show text on screen (HUD)
- (optional) make something orbit

This sandbox is the ramp-up to our Space Adventure missions later.

---

## What you need installed

### 1) Python
You should already have Python installed.

### 2) Pygame
Run this in PowerShell / Terminal:

python -m pip install pygame
````

✅ Test Pygame works:


python -c "import pygame; print(pygame.__version__)"
```

> On Windows, use `python`, not `python3`.
## ⭐ Deliverable 3 — Starfield Background (Pygame)

### Goal
Add a simple **starfield background** so space doesn’t look empty.  
Stars should **stay in the same place** every frame (not flicker).

This teaches:
- importing modules
- lists
- loops
- drawing with pygame
- separating setup from drawing

---

### Step 1 — Import `random`
Add this at the top with the other imports:

```python
import random

stars = []

for _ in range(15):  # try 5–20 stars
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    stars.append((x, y))

for star in stars:
    pygame.draw.circle(screen, (200, 200, 220), star, 1)

Why this works

stars is a list of fixed positions

The same stars are drawn every frame

No flicker = correct game loop structure

Common mistakes

Creating stars inside the game loop (causes flicker)

Forgetting import random

Using random.randint() every frame

