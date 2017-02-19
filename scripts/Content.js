import * as React from 'react';

import { ChatBot } from './ChatBot';
import { Button } from './Button';
import { TextArea } from './TextArea';

export class Content extends React.Component {
    render() {
        return (
            <div>
                <h1>Chat Room: </h1>
                <ChatBot />
                    <div
                         className="fb-login-button"
                         data-max-rows="1"
                         data-size="medium"
                         data-show-faces="false"
                         data-auto-logout-link="true">
                     </div>
                <TextArea />
            
                <div className="form-group">
                    <label htmlFor="comment"></label>
                        <input type="text" placeholder="Type a message" id="comment"/> 
                    <Button />
                </div>
            </div>
        );
    }
}
