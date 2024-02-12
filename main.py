import pygame, math, random

GRAVITY = 1
WIDTH = 2000
HEIGHT = 1500

class Particle():
	def __init__(self, x, y, size=10, col=(255,255,255), mass=1):
		self.x = x
		self.y = y
		self.size = size
		self.col = col
		self.weight = mass*GRAVITY
		self.xvel = 10
		self.yvel = 0

	def gravity(self):
		damper = 0.9
		self.yvel += GRAVITY
		if self.y >= HEIGHT and self.yvel >= 0:
			self.yvel = -self.yvel * damper

	def wall(self):
		damper = 0.5
		if (self.x >= WIDTH) or (self.x <= 0):
			if self.x >= WIDTH:#this is debugginh bcs the damper doesnt work without it, remove for speed later
				self.x = WIDTH-1
			else:
				self.x = 1
			self.xvel = -self.xvel * damper
		elif self.y <= 0:
			self.yvel = -self.yvel * damper
	def update(self):
		self.x += self.xvel
		self.y += self.yvel
		self.draw()

	def draw(self):
		pygame.draw.circle(screen, self.col, (self.x, self.y), self.size)

	def collision(self, particle_pos):
		#could do this by having a list of all particles will try next and see time efficientcy

		x1 = particle_pos[0]
		y1 = particle_pos[1]
		x2 = self.x
		y2 = self.y

		# pythag to see the magnitude of the vector between two particles
		radius = math.sqrt((x1-x2)**2 + (y1-y2)**2)
		#print(self.col, x1, y1, x2, y2, radius)

		#give appropriate force based on how close the particles are
		if radius > 50:
			force = 1
		elif radius <25 and radius > 10:
			force = 1.1
		else:

			force = 1.2

		#print(self.xvel, self.yvel)
		if force != 1:
			#apply the force to the particle
			self.xvel = -self.xvel * force
			self.yvel = -self.yvel * force
		#print(self.xvel, self.yvel)



if __name__ =='__main__':
	pygame.init()
	
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption = 'particle test'
	clock = pygame.time.Clock()

	ball1 = Particle(500,500)
	particle_list = []
	particle_list.append(ball1)

	ball2 = Particle(600,500)
	ball2.col = (0,0,0)
	ball2.xvel = -10
	particle_list.append(ball2)

	for i in range(10):
		particle = Particle(random.randint(0, WIDTH-100),random.randint(400,600))
		particle.xvel = random.randint(-10,10)
		particle.yvel = random.randint(-10,10)
		particle_list.append(particle)

	particle_pos = []
	for each in particle_list:
		particle_pos.append((each.x, each.y))
	'''
	for angle in range(360):
		angle = math.radians(angle)
		print(angle)
		x = int(500 + 100 * math.cos(angle))
		y = int(500 + 100 *  math.sin(angle))
		ball = Particle(x,y)
		particle_list.append(ball)'''
	for each in particle_list:
		each.draw()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		for each in particle_list:
			each.gravity()
			each.update()
			each.wall()
			for i in particle_list:
				if i == each:
					pass
				else:
					particle_pos = [i.x, i.y]
					each.collision(particle_pos)

		clock.tick(60)
		
		pygame.display.flip()
		#input()
		screen.fill((0,222,0))