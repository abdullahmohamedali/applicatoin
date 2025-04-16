for obj in tmx_data.get_layer_by_name('Trees'):
    Tree(
        pos=(obj.x, obj.y),
        surf=obj.image,
        groups=[self.all_sprites, self.collision_sprites, self.tree_sprites],
        name=obj.name,
        all_sprites=self.all_sprites,
        player_add=self.player_add
    )


    def player_add(self, item):
        self.player.item_inventory[item] += 1

        print(self.player.item_inventory)