/** @odoo-module **/

import {Counter} from "./counter/counter";
import {Component} from "@odoo/owl";

export class Playground extends Component {
    static template = "owl_component.playground";
    static components = {Counter};
}
