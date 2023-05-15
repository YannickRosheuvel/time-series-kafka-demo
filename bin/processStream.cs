using System;
using Confluent.Kafka;

namespace KafkaConsumer
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length < 1)
            {
                Console.WriteLine("Usage: dotnet run <topic>");
                return;
            }

            var topic = args[0];
            // var topic = "my-stream";

            var conf = new ConsumerConfig
            {
                BootstrapServers = "localhost:9092",
                GroupId = Environment.MachineName,
                AutoOffsetReset = AutoOffsetReset.Earliest
            };

            using (var consumer = new ConsumerBuilder<Ignore, string>(conf).Build())
            {
                consumer.Subscribe(topic);

                try
                {
                    while (true)
                    {
                        var msg = consumer.Consume();
                        if (msg == null) continue;

                        if (msg.IsPartitionEOF)
                        {
                            Console.Error.WriteLine($"% {msg.Topic} [{msg.Partition}] reached end at offset {msg.Offset}");
                        }
                        else
                        {
                            MsgProcess(msg);
                        }
                    }
                }
                catch (OperationCanceledException)
                {
                    // Cancelled
                    Console.Error.WriteLine("Errorrrr");
                }
                finally
                {
                    consumer.Close();
                }
            }
        }

        static void MsgProcess(ConsumeResult<Ignore, string> msg)
        {
            Console.WriteLine("Great Succes");
        }
    }
}
