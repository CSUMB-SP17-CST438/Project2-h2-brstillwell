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
                    'picture': "static/tom2.jpg",
                    'number': "Myspace is better"
                });
            }
            else if (commands[1] == "help")
            {
                Socket.emit('new message', {
                    'type': 'Bot',
                    'name': "TomBot",
                    'picture': "static/tom2.jpg",
                    'number': "commands: /\n/" +
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
                    'picture': "static/tom2.jpg",
                    'number': speak
                });
            }
        };
        module.exports.ChattyBot = Bot;
        return( 
            <p></p>
            );
    }
}
