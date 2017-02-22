import * as React from 'react';
import { Socket } from './Socket';

export class ChatBot extends React.Component {
    render() {
        var Bot = function ChattyBot(text){
            var commands = text.split(' ');
            if (commands[1] == "about")
            {
                Socket.emit('new message', {
                    'type': 'Bot',
                    'name': "TomBot",
                    'picture': "static/img/tom2.jpg",
                    'number': "Myspace is better"
                });
            }
            else if (commands[1] == "help")
            {
                Socket.emit('new message', {
                    'type': 'Bot',
                    'name': "TomBot",
                    'picture': "static/img/tom2.jpg",
                    'number': "!! say: Make bot say something"
                });
                Socket.emit('new message', {
                    'type': 'Bot',
                    'name': "TomBot",
                    'picture': "static/img/tom2.jpg",
                    'number': "!! about: Tells about the bot"
                });
                Socket.emit('new message', {
                    'type': 'Bot',
                    'name': "TomBot",
                    'picture': "static/img/tom2.jpg",
                    'number': "!! weather: Gives current weather forecast"
                });
                Socket.emit('new message', {
                    'type': 'Bot',
                    'name': "TomBot",
                    'picture': "static/img/tom2.jpg",
                    'number': "!! joke: Tells a joke"
                });
            }
            else if (commands[1] == "say")
            {
                var speak = "";
                for (var i = 2; i < commands.length; i++)
                {
                    speak = speak + " " + commands[i];
                }
                Socket.emit('new message', {
                    'type': 'Bot',
                    'name': "TomBot",
                    'picture': "static/img/tom2.jpg",
                    'number': speak
                });
            }
            else if (commands[1] == "weather")
            {
                Socket.emit('new message', {
                    'type': 'weather',
                    'name': "TomBot",
                    'picture': "static/img/tom2.jpg",
                    'number': "Here is the weather"
                });
            }
            else if (commands[1] == "joke")
            {
                Socket.emit('new message' , {
                    'type': 'Bot',
                    'name': 'TomBot',
                    'picture': "static/img/tom2.jpg",
                    'number': "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water."
                })
            }
            else
            {
                Socket.emit('new message' , {
                    'type': 'Bot',
                    'name': 'TomBot',
                    'picture': "static/img/tom2.jpg",
                    'number': "Unrecognized command: " + text
                })
            }
        };
        module.exports.ChattyBot = Bot;
        return( 
            <p></p>
            );
    }
}
