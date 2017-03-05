import * as React from 'react';
import { Socket } from './Socket';

export class ChatBot extends React.Component {
    render() {
        var Bot = function ChattyBot(text){
            Socket.emit('chatbot message', {
                'text': text
            });
        };
        module.exports.ChattyBot = Bot;
        return( 
            <p></p>
            );
    }
}
