figure(1)
T=length(out.theta.Data);
hold off
r = 0.02825
L = 0.105
for i=1:T;
    x = [r*out.pshi.Data(i,1) r*out.pshi.Data(i,1)+L*sin(out.theta.Data(i,1))];
    y = [0 L*cos(out.theta.Data(i,1))];
    plot(r * out.pshi.Data(i,1),0,'-o','MarkerSize',40);
    line(x,y,'Color','red','LineWidth',6)
    hold off
    axis([-0.1 0.1 -0.05 0.15]);
    drawnow;
    pause(0.001)
end
close all;