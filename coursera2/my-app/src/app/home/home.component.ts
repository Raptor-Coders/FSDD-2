import { Component, OnInit } from '@angular/core';
import { COURSES } from '../courses-data';
import { CourseService, getMyName2 } from '../course.service';
import { IcourseInterface } from '../icourse.interface';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})


export class HomeComponent implements OnInit {
  featuredCourses: IcourseInterface[] = [];

  constructor(private courseService: CourseService) {}
  ngOnInit(): void {
    this.getCourses();
  }

  getCourses(): void {
    this.courseService.getFeaturedCourses().subscribe(fCourses => {
      this.featuredCourses = fCourses;
      console.log(this.featuredCourses)
    });
  }
}
