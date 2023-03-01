import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class AdafruitIOPublisher {

    public static void main(String[] args) {

        String topic = "joaof9352/feeds/feedteste";
        String broker = "tcp://io.adafruit.com:1883";
        String clientId = "JavaSample";
        MemoryPersistence persistence = new MemoryPersistence();

        try {
            MqttClient client = new MqttClient(broker, clientId, persistence);
            MqttConnectOptions connOpts = new MqttConnectOptions();
            //connOpts.setUserName("");
            //connOpts.setPassword("".toCharArray());
            client.connect(connOpts);
            String content = "Hello World";
            MqttMessage message = new MqttMessage(content.getBytes());
            message.setQos(2);
            client.publish(topic, message);
            System.out.println("Mensagem publicada: " + content);
        } catch (MqttException e) {
            e.printStackTrace();
        }

    }
}
