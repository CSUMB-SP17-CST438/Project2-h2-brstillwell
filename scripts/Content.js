import * as React from 'react';

import { ChatBot } from './ChatBot';
import { Button } from './Button';
import { TextArea } from './TextArea';
import { Users } from './Users';
import { CurrentUsers } from './CurrentUsers';

export class Content extends React.Component {
    render() {
        return (
            <div id="UI">
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
                    <img src="https://mail.google.com/mail/u/0/?logout&hl=en" />
                </h1>
                <div id="content">
                    <div id="userBox">
                        <CurrentUsers />
                        <Users />
                    </div>
                    <TextArea />
                        <input type="text" placeholder="Type a message" id="comment" /> 
                        <Button id="buttonWrapper"/>
                </div>
              
                <ChatBot />
            </div>
        );
    }
}
