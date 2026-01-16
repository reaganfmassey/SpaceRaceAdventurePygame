
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
- why we separate *setup* from *draw*

---

### What you are adding
You will:
1. Import the `random` module
2. Create a **list of stars** (once)
3. Draw those stars **every frame**

---

### Step 1 — Import `random`
At the top of the file with the other imports:

```python
import random
Step 2 — Create a stars list (SETUP, outside the game loop)
Add this once, near the top of the file (after planets is fine):

python
Copy code
stars = []

for _ in range(15):  # try 5–20 stars
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    stars.append((x, y))
✅ This only runs one time
❌ Do NOT put this inside the while running: loop

Step 3 — Draw the stars (DRAW section)
Inside the main loop, after screen.fill(SPACE):

python
Copy code
for star in stars:
    pygame.draw.circle(screen, (200, 200, 220), star, 1)
This draws each star as a tiny dot.

Why this works
stars is a list of positions

We loop over it every frame

The positions don’t change → no flickering

This is how games reuse data every frame

Common mistakes (watch for these!)
❌ Creating stars inside the game loop (causes flicker)
❌ Forgetting import random
❌ Using random.randint() every frame
