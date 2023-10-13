class Elf:
    def __init__(self, pos):
        self.pos = pos
        self.will_move = False
        self.proposed_pos = None

    def propose_move(self, directions, elf_positions, proposed_moves):
        will_move = False
        proposed_move = []
        for nswe in directions:
            is_clear = True
            for i in range(0, len(nswe)):
                test_pos = (self.pos[0] + nswe[i][0], self.pos[1] + nswe[i][1])
                if str(test_pos) in elf_positions:
                    is_clear = False
                    will_move = True
            if is_clear and len(proposed_move) == 0:
                prop_move = (self.pos[0] + nswe[1][0], self.pos[1] + nswe[1][1])
                proposed_move.append(prop_move)
            #print(is_clear, will_move)
        if will_move and len(proposed_move) != 0:
            self.will_move = True
            self.proposed_pos = proposed_move[0]
            if str(proposed_move[0]) not in proposed_moves:
                proposed_moves[str(proposed_move[0])] = 1
            else:
                proposed_moves[str(proposed_move[0])] += 1
            #proposed_moves.add(str(proposed_move[0]))
        # else:
        #     #proposed_move.append(None)
        #     proposed_moves.add(None)
        # #return proposed_move[0]

    def check_proposed_move(self, proposed_moves_counts):
        if self.will_move:
            if proposed_moves_counts[str(self.proposed_pos)] > 1:
                self.will_move = False

    def move(self):
        has_moved = False
        if self.will_move:
            self.pos = self.proposed_pos
            self.will_move = False
            has_moved = True
        self.proposed_pos = None
        return has_moved


