export interface IcourseInterface {
  id: number;
  title: string;
  description: string;
  sessions: number;
  sessionDuration: number;
  startDate?: string;
  endDate?: string;
  tags: string[];
  isFeatured: boolean;
  imageUrl: string;
}
