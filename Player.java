


Public class AudioPlayer
{

public AudioPlayer()
{
System.out.println("The AudioPlayer constructor was invoked.");
isOpen = false;
isPlaying = false;
setVolume(10);
}

public void open(string filePath)
{
//@ToDo: por ahora simulamos la apertura correcta
isOpen = true;
System.out.println("The audiofile: "+ filePath +" is open.");
}
public void play()
{
//@ToDo: por ahora simulamos la reproducción correcta
if(isOpen) isPlaying = true;
System.out.println("The audiofile is playing.");
}
public void stop()
{
//@ToDo: por ahora simulamos la detención correcta
if(isPlaying) isPlaying = false;
system.out.println("The audiofile is stopped.");
}
public void setVolume(float value)
{
volume = value;
System.out.println("The volume value is: " + volume);
}
private bool isOpenbool isPlaying;
private float volume;
};


public class VLC {
  private class AudioPlayer
{
public class AudioPlayer
Public VLC()
{
System.out.println("The VLC constructor was invoked.");
setVolume(10);
setPitch(0);
}
piblic -VLC()
{
System.out.println("The VLC destructor was invoked." );
}
public void setPitch(float value)
{
pitch = value;
System.out.println("The pitch value is: " + pitch );
}
float pitch;
};

public class main()
{

public static void main(String[] args ){

System.out.println(/n);
AudioPlayer player;
player.open("./resources/orchestral.ogg");
player.play();
player.setVolume(4);
System.out.println(/n);
VLC vlcPlayer;
vlcPlayer.open("./resources/orchestral.ogg");
vlcPlayer.play();
vlcPlayer.setVolume(13);
System.out.println(/n);
return EXIT_SUCCESS;
}
}