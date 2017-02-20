import * as React from 'react';

import { ChatBot } from './ChatBot';
import { Button } from './Button';
import { TextArea } from './TextArea';
import { Users } from './Users';

export class Content extends React.Component {
    render() {
        return (
            <div>
                <h1>Chat Room: 
                    <div
                         className="fb-login-button"
                         data-max-rows="1"
                         data-size="large"
                         data-show-faces="false"
                         data-auto-logout-link="true">
                     </div>
                     <div
                        className="g-signin2"
                        data-theme="dark">
                    </div>
                     </h1>
                <Users />
                <TextArea />
                <span id="positionfix" />
                <div className="form-group">
                    <label htmlFor="comment"></label>
                        <input type="text" placeholder="Type a message" id="comment"/> 
                    <Button id="buttonSend"/>
                </div>
              
                <ChatBot />
            </div>
        );
    }
}
