import {Component, ElementRef, ViewChild} from '@angular/core';
import {PageService} from "./page.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  @ViewChild('section') section!: ElementRef;
  title = 'ac_front';
  constructor(public pageService: PageService) {}

  scrollToSection() {
    this.section.nativeElement.scrollIntoView({ behavior: 'smooth' });
  }
}
