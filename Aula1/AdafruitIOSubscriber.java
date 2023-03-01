import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class AdafruitIOSubscriber {

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
            client.subscribe(topic, 0);
            System.out.println("Subscrito ao feed: " + topic);

            client.setCallback(new MqttCallback() {
                public void connectionLost(Throwable cause) {}
                public void messageArrived(String topic, MqttMessage message) throws Exception {
                    System.out.println("Mensagem recebida: " + new String(message.getPayload()));
                }
                public void deliveryComplete(IMqttDeliveryToken token) {}
            });

        } catch (MqttException e) {
            e.printStackTrace();
        }

    }
}
