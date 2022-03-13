def gradient(x,y,w,b,c,batch_size,gw,gb,Gw,Gb):
    for i in range(batch_size):
        if(classificate(x[i],y[i],w,b)==1):
            gw=-y[i]*x[i]
            gb=-y[i]
        if(classificate(x[i],y[i],w,b)==0):
            gw=0
            gb=0
        Gw +=c * gw/batch_size  
        Gb += c * gb/batch_size  
    D=[-Gw,-Gb]
    return D