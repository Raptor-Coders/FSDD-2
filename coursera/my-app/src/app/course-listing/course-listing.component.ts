import { Component, OnInit } from '@angular/core';
import { COURSES } from '../courses-data';
import { CourseService } from '../course.service';
import { IcourseInterface } from '../icourse.interface';

@Component({
  selector: 'app-course-listing',
  templateUrl: './course-listing.component.html',
  styleUrls: ['./course-listing.component.css'],
})
export class CourseListingComponent implements OnInit {
  allCourses: IcourseInterface[] = [];
  // constructor(private courseService: CourseService) {
  //   this.allCourses = courseService.getAllCourses();
  // }
  constructor(private courseService: CourseService) {}
  ngOnInit(): void {
    this.getCourses();
  }

  getCourses(): void {
    this.courseService.getAllCourses().subscribe((courses) => {
      this.allCourses = courses;
      console.log(this.allCourses);
    });
  }
}
