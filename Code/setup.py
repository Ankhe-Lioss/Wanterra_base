from test import *
def setup(game):
    map = load_pygame(join('..', 'data', 'maps', 'Test_level.tmx'))
    for x, y, image in map.get_layer_by_name('Tile Layer 1').tiles():
        Sprite((x * TILE_SIZE, y * TILE_SIZE), image, game.all_sprites)
    for x, y, image in map.get_layer_by_name('Tile Layer 2').tiles():
        Sprite((x * TILE_SIZE, y * TILE_SIZE), image, game.all_sprites)
    for obj in map.get_layer_by_name('Objects'):
        CollisionSprite((obj.x, obj.y), obj.image, (game.all_sprites, game.collision_sprites))

    for obj in map.get_layer_by_name('Collisions'):
        CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), game.collision_sprites)

    for obj in map.get_layer_by_name('Entities'):
        if obj.name == 'Player':
            game.player = Player((obj.x, obj.y), game.all_sprites, game.collision_sprites)
            game.gun = Gun(game.player, game.all_sprites)
        else:
            if obj.name == 'Poro':
                Spawn_poro((obj.x, obj.y), game)
            if obj.name == 'Meele':
                Spawn_meele((obj.x, obj.y), game)