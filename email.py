import sendgrid

client = sendgrid.SenGridClient("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")
message = sendrig.Mail()

message.add_to("mmoreno@ids.upchiapas.edu.mx")
message.set_from("joxesandoval.24@gmail.com")
message.set_html("Prueba comd")
client.send(message)
