import * as React from 'react';
import { Socket } from './Socket';

export class ChatBot extends React.Component {
    render() {
        var Bot = function ChattyBot(text){
            var commands = text.split(' ');
            console.log("this is the correct function");
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
                    'number': "commands:/\n/" +
                                    "about/\n/" +
                                    "say <something>"
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
                console.log("weather chatbot");
                Socket.emit('new message', {
                    'type': 'weather',
                    'name': "TomBot",
                    'picture': "static/img/tom2.jpg",
                    'number': "Here is the weather"
                });
            }
            else if (commands[1] == "gif")
            {
                console.log("this is the gif");
                Socket.emit('new message' , {
                    'type': 'Bot',
                    'name': 'TomBot',
                    'picture': "static/img/tom2.jpg",
                    'number': "https://68.media.tumblr.com/b21481bb5d888c0df2163016294b0d83/tumblr_ola9cs6wTI1tx9mwqo1_500.gif"
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
