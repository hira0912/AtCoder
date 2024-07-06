def function():
    a,b,c,d,e,f = map(int,input().split())
    g,h,i,j,k,l = map(int,input().split())

    def calc(p1,p2,p3,p4):
        if(p1<=p2):
            par1L=p1
            par1R=p2
        else:
            par1L=p2
            par1R=p1
        if(p3<=p4):
            par2L=p3
            par2R=p4
        else:
            par2L=p4
            par2R=p3        
        if((par1L<par2L and par1R<=par2L) or (par2L<par1L and par2R<=par1L)):
            return False
        return True
    
    if(calc(a,d,g,j)==False):
        print('No')
        return
    if(calc(b,e,h,k)==False):
        print('No')
        return
    if(calc(c,f,i,l)==False):
        print('No')
        return
    print('Yes') 
    return   

if __name__ == "__main__":
    function()