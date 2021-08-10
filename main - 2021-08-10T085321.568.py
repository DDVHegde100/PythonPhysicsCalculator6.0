print("Welcome to Dhruv's Physics Calculator")
calc=str(input('Enter the calculation(no capital letters): '))

if(calc=='velocity'):
    displacement=float(input('Enter the displacement:'))
    time=float(input('Enter the time:'))
    velocity=displacement/time
    print('%0.3f is the output velocity.' %(velocity))
elif(calc=='acceleration'):
    velocity2=float(input('Enter the velocity:'))
    time2=float(input('Enter the time:'))
    acceleration=velocity2/(time2)*(time2)
    print('%0.3f is the output acceleration.' %(acceleration))
elif(calc=='force'):
    mass=float(input('Enter the mass:'))
    acceleration2=float(input('Enter the acceleration:'))
    force=mass*acceleration2
    print('%0.3f is the output force.' %(force))
elif(calc=='weight'):
    mass2=float(input('Enter the mass:'))
    gravity=9.8
    weight=mass*gravity
    print('%0.3f is the weight.' %(weight))
elif(calc=='work'):
    force2=float(input('Enter the force:'))
    distance=float(input('Enter the distance:'))
    work=force2*distance
    print('%0.3f is the work.' %(work))
elif(calc=='power'):
    work2=float(input('Enter the work:'))
    time3=float(input('Enter the time:'))
    power=work2/time3
    print('%0.3f is the power.' %(power))