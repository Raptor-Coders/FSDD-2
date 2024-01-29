import { Component } from '@angular/core';
import { COURSES } from '../courses-data';
import { CourseService, getMyName2 } from '../course.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  featuredCourses: any = [];

  // myName: string;

  myName2: string = getMyName2();

  constructor(private courseService: CourseService) {
    this.featuredCourses = courseService.getFeaturedCourses();
    console.log(this.featuredCourses)
    // this.myName = courseService.getMyName();
  }
}
