from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def put_in_place(self,g,k):
        ligne_k,colone_k=k//g.n,k%g.n
        for i in range(g.m):
            for j in range (g.n):
                if g.state[i][j]==k+1: 
                    cell1=(i,j)
                    break
        h=[]
        i,j=cell1
        if j<colone_k :
            while j!=colone_k:
                h.append (((i,j),(i,j+1)))
                j+=1
        else :
            while j!=colone_k:
                h.append (((i,j),(i,j-1)))
                j-=1
        if i<ligne_k:
            while i!= ligne_k:
                h.append (((i,colone_k),(i+1,colone_k)))
                i+=1
        else :
            while i!= ligne_k:
                h.append (((i,colone_k),(i-1,colone_k)))
                i-=1
        g.swap_seq(h)
        return h

    def get_solution(self,g):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        h=[]
        for k in range(g.n*g.m):
            h+=self.put_in_place(g,k)
        return h



g=Grid(10,10,[])

s=Solver()
g.swap_seq([((3,5),(3,6)),((4,7),(4,8))])
h=s.get_solution(g)
print(h)